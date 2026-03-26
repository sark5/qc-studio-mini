import streamlit.components.v1 as components
import base64

def show_niivue(uploaded_file, height=520):
    """Render Niivue directly from uploaded file (supports .nii and .nii.gz)"""

    # Read file and encode
    file_bytes = uploaded_file.getvalue()
    b64 = base64.b64encode(file_bytes).decode()

    # Detect compression
    is_compressed = str(uploaded_file.name.lower().endswith(".gz")).lower()

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            html, body {{ margin:0; height:100%; overflow:hidden; }}
            canvas {{ width:100%; height:100%; display:block; }}
        </style>
    </head>
    <body>
        <canvas id="gl"></canvas>

        <script type="module">
            import {{ Niivue }} from "https://unpkg.com/@niivue/niivue@0.57.0/dist/index.js";

            async function main() {{
                const nv = new Niivue({{
                    isResizeCanvas: true,
                    backColor: [0, 0, 0, 1]
                }});

                await nv.attachTo("gl");

                // Decode base64 → Uint8Array
                const byteCharacters = atob("{b64}");
                const byteNumbers = new Array(byteCharacters.length);

                for (let i = 0; i < byteCharacters.length; i++) {{
                    byteNumbers[i] = byteCharacters.charCodeAt(i);
                }}

                const byteArray = new Uint8Array(byteNumbers);

                // Create blob + URL
                const blob = new Blob([byteArray], {{ type: "application/octet-stream" }});
                const url = URL.createObjectURL(blob);

                // Load MRI volume
                await nv.loadVolumes([{{
                    url: url,
                    name: "{uploaded_file.name}",
                    isCompressed: {is_compressed}
                }}]);

                // Optional: better default view
                nv.setSliceType(nv.sliceTypeMultiplanar);
                nv.opts.crosshairColor = [1, 0, 0, 1];
                nv.updateGLVolume();
            }}

            main();
        </script>
    </body>
    </html>
    """

    components.html(html_code, height=height, scrolling=False)