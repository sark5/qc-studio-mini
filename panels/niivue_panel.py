import streamlit.components.v1 as components
import base64


def show_niivue(uploaded_file, height=520):
    if uploaded_file is None:
        return

    file_bytes = uploaded_file.getvalue()
    b64 = base64.b64encode(file_bytes).decode()
    is_compressed = str(uploaded_file.name.lower().endswith(".gz")).lower()

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            html, body {{ margin:0; height:100%; overflow:hidden; background:#111; }}
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
                    backColor: [0.08, 0.08, 0.08, 1]
                }});

                await nv.attachTo("gl");

                const byteCharacters = atob("{b64}");
                const byteNumbers = new Array(byteCharacters.length);

                for (let i = 0; i < byteCharacters.length; i++) {{
                    byteNumbers[i] = byteCharacters.charCodeAt(i);
                }}

                const byteArray = new Uint8Array(byteNumbers);
                const blob = new Blob([byteArray], {{ type: "application/octet-stream" }});
                const url = URL.createObjectURL(blob);

                await nv.loadVolumes([{{
                    url: url,
                    name: "{uploaded_file.name}",
                    isCompressed: {is_compressed}
                }}]);

                nv.setSliceType(nv.sliceTypeMultiplanar);
                nv.opts.crosshairColor = [1, 0.2, 0.2, 1];
                nv.updateGLVolume();
            }}

            main();
        </script>
    </body>
    </html>
    """

    components.html(html_code, height=height, scrolling=False)