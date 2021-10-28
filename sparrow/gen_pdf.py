import numpy as np
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def get_pdf_sample():
    np.random.seed(24)
    test_df = pd.DataFrame({"A": np.linspace(1, 10, 10)})
    test_df = pd.concat([test_df, pd.DataFrame(np.random.randn(10, 4), columns=list("BCDE"))], axis=1)
    test_df.iloc[3, 3] = np.nan
    test_df.iloc[0, 2] = np.nan
    env = Environment(autoescape=True, loader=FileSystemLoader("."))
    template = env.get_template("test.html")
    template_args = {"table": test_df.style.render()}
    html_test = template.render(template_args)
    with open("test1.html", "w", encoding="utf8") as test1:
        test1.write(html_test)
    HTML(string=html_test, base_url="./").write_pdf("test.pdf")
