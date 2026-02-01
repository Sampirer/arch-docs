#!/usr/bin/env python3
"""Parse WoW TBC talent calculator data from Wowhead or Icy Veins.

This script extracts build allocation strings from calculator URLs, then
attempts to parse talent metadata from downloaded HTML. If rich data cannot be
parsed, it will still return a structured JSON payload with raw data attached
for later inspection.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import re
import sys
import textwrap
from html import unescape
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen


@dataclasses.dataclass
class TalentEffect:
    effect_type: str
    value: Optional[float]
    unit: Optional[str]
    raw_text: str


@dataclasses.dataclass
class TalentRank:
    rank: int
    effects: List[TalentEffect]
    raw_text: str


@dataclasses.dataclass
class TalentNode:
    node_id: str
    name: str
    max_rank: int
    tier: int
    column: int
    prerequisites: List[str]
    ranks: List[TalentRank]


@dataclasses.dataclass
class TalentTree:
    tree_id: str
    name: str
    order: int
    nodes: List[TalentNode]


@dataclasses.dataclass
class TalentBuild:
    source: str
    game: str
    class_name: str
    raw_allocation: str
    trees: List[TalentTree]
    raw_metadata: Dict[str, Any]


WOWHEAD_HOST = "www.wowhead.com"
ICY_VEINS_HOST = "www.icy-veins.com"
USER_AGENT = "Mozilla/5.0 (TalentParser/1.0; +https://example.local)"


def fetch_html(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=30) as response:
        content = response.read()
    return content.decode("utf-8", errors="ignore")


def parse_url(url: str) -> Tuple[str, str, str, str]:
    parsed = urlparse(url)
    host = parsed.netloc
    path = parsed.path.strip("/")
    fragment = parsed.fragment

    if host.endswith(WOWHEAD_HOST):
        parts = path.split("/")
        try:
            class_name = parts[-2]
            raw_allocation = parts[-1]
        except IndexError:
            raise ValueError("Unexpected Wowhead URL format.")
        return "wowhead", "tbc-classic", class_name, raw_allocation

    if host.endswith(ICY_VEINS_HOST):
        class_name = path.split("/")[-1].replace("-talent-calculator", "")
        raw_allocation = fragment.replace("tc-", "")
        return "icy-veins", "tbc-classic", class_name, raw_allocation

    raise ValueError("Unsupported URL host: {host}".format(host=host))


def extract_script_blocks(html: str) -> Iterable[str]:
    for match in re.finditer(r"<script[^>]*>(.*?)</script>", html, re.S | re.I):
        yield match.group(1)


def find_js_object(script: str, markers: Iterable[str]) -> Optional[str]:
    for marker in markers:
        index = script.find(marker)
        if index == -1:
            continue
        brace_index = script.find("{", index)
        if brace_index == -1:
            continue
        return extract_braced_block(script, brace_index)
    return None


def extract_braced_block(text: str, start_index: int) -> Optional[str]:
    depth = 0
    for i in range(start_index, len(text)):
        char = text[i]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start_index : i + 1]
    return None


def normalize_js_object(js_text: str) -> str:
    normalized = js_text
    normalized = re.sub(r"/\*.*?\*/", "", normalized, flags=re.S)
    normalized = re.sub(r"//.*", "", normalized)
    normalized = normalized.replace("undefined", "null")
    normalized = normalized.replace("true", "true").replace("false", "false")
    normalized = re.sub(r"(\b[a-zA-Z_][a-zA-Z0-9_]*\b)\s*:", r'"\1":', normalized)
    normalized = normalized.replace("'", '"')
    normalized = re.sub(r",\s*([}\]])", r"\1", normalized)
    return normalized


def parse_js_object(js_text: str) -> Optional[Dict[str, Any]]:
    normalized = normalize_js_object(js_text)
    try:
        return json.loads(normalized)
    except json.JSONDecodeError:
        return None


def extract_wowhead_data(html: str) -> Dict[str, Any]:
    markers = [
        "talentCalc",
        "talentCalculator",
        "g_talent",
        "talentData",
    ]
    raw_data: Dict[str, Any] = {"blocks": []}
    for script in extract_script_blocks(html):
        block = find_js_object(script, markers)
        if not block:
            continue
        parsed = parse_js_object(block)
        raw_data["blocks"].append({"raw": block, "parsed": parsed})
    return raw_data


def extract_icy_veins_data(html: str) -> Dict[str, Any]:
    markers = ["talent", "tree", "calculator"]
    raw_data: Dict[str, Any] = {"blocks": []}
    for script in extract_script_blocks(html):
        block = find_js_object(script, markers)
        if not block:
            continue
        parsed = parse_js_object(block)
        raw_data["blocks"].append({"raw": block, "parsed": parsed})
    return raw_data


def normalize_tree_data(raw_data: Dict[str, Any]) -> List[TalentTree]:
    trees: List[TalentTree] = []
    for block in raw_data.get("blocks", []):
        parsed = block.get("parsed") or {}
        if not isinstance(parsed, dict):
            continue
        data_trees = parsed.get("trees") or parsed.get("talentTrees")
        if not data_trees:
            continue
        for order, tree in enumerate(data_trees):
            tree_id = str(tree.get("id", tree.get("name", order))).lower()
            nodes: List[TalentNode] = []
            for talent in tree.get("talents", []):
                node_id = str(talent.get("id", talent.get("name", "unknown"))).lower()
                ranks = []
                for rank_index, rank in enumerate(talent.get("ranks", []), start=1):
                    raw_text = unescape(str(rank))
                    ranks.append(
                        TalentRank(
                            rank=rank_index,
                            effects=[
                                TalentEffect(
                                    effect_type="raw",
                                    value=None,
                                    unit=None,
                                    raw_text=raw_text,
                                )
                            ],
                            raw_text=raw_text,
                        )
                    )
                nodes.append(
                    TalentNode(
                        node_id=node_id,
                        name=str(talent.get("name", "")),
                        max_rank=int(talent.get("maxRank", len(ranks) or 1)),
                        tier=int(talent.get("tier", 0)),
                        column=int(talent.get("column", 0)),
                        prerequisites=talent.get("requires", []),
                        ranks=ranks,
                    )
                )
            trees.append(
                TalentTree(
                    tree_id=tree_id,
                    name=str(tree.get("name", "")),
                    order=order,
                    nodes=nodes,
                )
            )
    return trees


def build_output(
    source: str,
    game: str,
    class_name: str,
    raw_allocation: str,
    raw_metadata: Dict[str, Any],
) -> TalentBuild:
    trees = normalize_tree_data(raw_metadata)
    return TalentBuild(
        source=source,
        game=game,
        class_name=class_name,
        raw_allocation=raw_allocation,
        trees=trees,
        raw_metadata=raw_metadata,
    )


def load_html(url: Optional[str], html_file: Optional[str]) -> Optional[str]:
    if html_file:
        with open(html_file, "r", encoding="utf-8") as handle:
            return handle.read()
    if url:
        return fetch_html(url)
    return None


def parse_talent_data(url: Optional[str], html_file: Optional[str]) -> TalentBuild:
    if not url and not html_file:
        raise ValueError("Provide a URL or an HTML file to parse.")

    if url:
        source, game, class_name, raw_allocation = parse_url(url)
    else:
        source = "unknown"
        game = "tbc-classic"
        class_name = "unknown"
        raw_allocation = ""

    html = load_html(url, html_file)
    if not html:
        return TalentBuild(
            source=source,
            game=game,
            class_name=class_name,
            raw_allocation=raw_allocation,
            trees=[],
            raw_metadata={},
        )

    if source == "wowhead":
        raw_metadata = extract_wowhead_data(html)
    elif source == "icy-veins":
        raw_metadata = extract_icy_veins_data(html)
    else:
        raw_metadata = {"htmlSnippet": html[:5000]}

    return build_output(source, game, class_name, raw_allocation, raw_metadata)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Parse WoW TBC talent calculator data into structured JSON.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """
            Examples:
              python tools/wow_talent_parser.py \
                --url https://www.wowhead.com/tbc/talent-calc/warlock/1502... \
                --output warlock.json

              python tools/wow_talent_parser.py \
                --html-file saved.html --source icy-veins --output out.json
            """
        ),
    )
    parser.add_argument("--url", help="Talent calculator URL to parse.")
    parser.add_argument("--html-file", help="Local HTML file to parse.")
    parser.add_argument("--output", help="Output JSON file (defaults to stdout).")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    try:
        build = parse_talent_data(args.url, args.html_file)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    payload = dataclasses.asdict(build)
    output = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(output + "\n")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
