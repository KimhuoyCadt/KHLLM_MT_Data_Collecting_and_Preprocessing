
import os
import json
import glob

INPUT_FOLDER = "v2_clean_mt_dataset"
OUTPUT_ROOT = "v3_clean_mt_dataset"

CHUNK_SIZE = 10000

MIN_LEN = 3
MAX_LEN = 500
MIN_RATIO = 0.5
MAX_RATIO = 2.0

os.makedirs(OUTPUT_ROOT, exist_ok=True)


def is_valid(record):
    try:
        if record["metadata"]["is_flagged"]:
            return False

        src = record["source_text"].strip()
        tgt = record["target_text"].strip()

        if not src or not tgt:
            return False

        if len(src) < MIN_LEN or len(tgt) < MIN_LEN:
            return False

        if len(src) > MAX_LEN or len(tgt) > MAX_LEN:
            return False

        ratio = record["stats"]["length_ratio"]

        if ratio < MIN_RATIO or ratio > MAX_RATIO:
            return False

        if record["stats"]["source"]["has_html"]:
            return False

        return True

    except:
        return False


def open_chunk(folder, chunk_num):

    km_out = open(
        os.path.join(
            folder,
            f"chunk_{chunk_num:04d}.km"
        ),
        "w",
        encoding="utf-8"
    )

    en_out = open(
        os.path.join(
            folder,
            f"chunk_{chunk_num:04d}.en"
        ),
        "w",
        encoding="utf-8"
    )

    return km_out, en_out


def process_one_file(file_path):

    base_name = os.path.splitext(
        os.path.basename(file_path)
    )[0]

    output_folder = os.path.join(
        OUTPUT_ROOT,
        base_name
    )

    os.makedirs(output_folder, exist_ok=True)

    total = 0
    kept = 0
    filtered = 0

    chunk_num = 1
    pair_count = 0

    km_out, en_out = open_chunk(
        output_folder,
        chunk_num
    )

    with open(file_path, "r", encoding="utf-8") as f:

        for line in f:

            total += 1

            try:
                record = json.loads(line)

                if is_valid(record):

                    src = record["source_text"].strip()
                    tgt = record["target_text"].strip()

                    if pair_count >= CHUNK_SIZE:

                        km_out.close()
                        en_out.close()

                        chunk_num += 1
                        pair_count = 0

                        km_out, en_out = open_chunk(
                            output_folder,
                            chunk_num
                        )

                    km_out.write(src + "\n")
                    en_out.write(tgt + "\n")

                    kept += 1
                    pair_count += 1

                else:
                    filtered += 1

            except:
                filtered += 1

    km_out.close()
    en_out.close()

    summary = {
        "input_file": os.path.basename(file_path),
        "chunks_created": chunk_num,
        "total_records": total,
        "kept_pairs": kept,
        "filtered_out": filtered,
        "keep_ratio": (
            kept / total if total else 0
        )
    }

    with open(
        os.path.join(
            output_folder,
            "summary.json"
        ),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            summary,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(f"Done: {base_name}")


def main():

    files = glob.glob(
        os.path.join(
            INPUT_FOLDER,
            "*.jsonl"
        )
    )

    for file in files:
        process_one_file(file)


if __name__ == "__main__":
    main()

