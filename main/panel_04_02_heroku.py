import panel as pn

pn.extension()

# シンプルなPanelアプリケーション
def app():
    return pn.Column("### My Panel App", pn.widgets.Button(name="Click Me"))

# サーバーとして起動
app().servable()
pn.serve(app)
