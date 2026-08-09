import os
import re

pub_dir = "content/publication"

if os.path.exists(pub_dir):
    updated_count = 0
    for folder in os.listdir(pub_dir):
        index_file = os.path.join(pub_dir, folder, "index.md")
        if os.path.isfile(index_file):
            with open(index_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Check for legacy url_pdf field
            match = re.search(r'^url_pdf:\s*"([^"]+)"', content, flags=re.MULTILINE)
            if match:
                pdf_url = match.group(1)
                # Replace url_pdf line with new links block
                new_links_str = f'links:\n  - type: pdf\n    url: "{pdf_url}"'
                updated_content = re.sub(
                    r"^url_pdf:\s*.*$",
                    new_links_str,
                    content,
                    flags=re.MULTILINE,
                )

                with open(index_file, "w", encoding="utf-8") as f:
                    f.write(updated_content)

                updated_count += 1

    print(
        f"Successfully updated {updated_count} files to the new links format."
    )