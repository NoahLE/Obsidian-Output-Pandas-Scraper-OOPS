import pandas as pd


def parse_plugins():
    dfp = pd.read_json("community-plugins.json", orient="records")
    dfp = dfp[["id", "name", "description", "repo"]]
    dfp["repo"] = dfp["repo"].apply(
        lambda repo: f"<a href='https://github.com/{repo}'>{repo}</a>"
    )

    dfps = pd.read_json("community-plugin-stats.json", orient="index")
    dfps["id"] = dfps.index
    dfps = dfps[["id", "downloads"]]

    df = dfp.merge(dfps, on="id")
    df = df[df["downloads"] > 300000]
    df.sort_values("downloads")

    df = df[["name", "repo", "description", "downloads"]]

    df.to_html(
        "top-plugins.html",
        index=False,
        justify="center",
        render_links=True,
        escape=False,
    )


if __name__ == "__main__":
    parse_plugins()
