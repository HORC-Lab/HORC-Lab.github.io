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

            pdf_url = None

            # 1. Extract URL from any existing links block
            match_links = re.search(
                r'url:\s*"([^"]+\.pdf)"', content, re.IGNORECASE
            )
            if match_links:
                pdf_url = match_links.group(1)

            # 2. Extract existing url_pdf if present
            if not pdf_url:
                match_url_pdf = re.search(
                    r'^url_pdf:\s*"([^"]+)"', content, flags=re.MULTILINE
                )
                if match_url_pdf and match_url_pdf.group(1).strip():
                    pdf_url = match_url_pdf.group(1)

            # 3. Fallback: check static/pdf/ or static/papers/ for matching folder name
            if not pdf_url:
                if os.path.exists(os.path.join("static", "pdf", f"{folder}.pdf")):
                    pdf_url = f"/pdf/{folder}.pdf"
                elif os.path.exists(os.path.join("static", "papers", f"{folder}.pdf")):
                    pdf_url = f"/papers/{folder}.pdf"

            if pdf_url:
                # Remove temporary/broken links block if created previously
                cleaned = re.sub(
                    r'links:\s*\n\s*-\s*type:\s*pdf\s*\n\s*url:\s*"[^"]+"\n?',
                    "",
                    content,
                )

                # Set or update url_pdf in front matter
                url_pdf_pattern = r"^url_pdf:\s*.*$"
                if re.search(url_pdf_pattern, cleaned, flags=re.MULTILINE):
                    cleaned = re.sub(
                        url_pdf_pattern,
                        f'url_pdf: "{pdf_url}"',
                        cleaned,
                        flags=re.MULTILINE,
                    )
                else:
                    parts = cleaned.split("---", 2)
                    if len(parts) >= 3:
                        parts[1] = parts[1].strip() + f'\nurl_pdf: "{pdf_url}"'
                        cleaned = "---" + parts[1] + "\n---" + parts[2]

                if cleaned != content:
                    with open(index_file, "w", encoding="utf-8") as f:
                        f.write(cleaned)
                    updated_count += 1

    print(f"Successfully restored url_pdf in {updated_count} publication files.")