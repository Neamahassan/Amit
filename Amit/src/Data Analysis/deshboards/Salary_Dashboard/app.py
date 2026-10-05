import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output

# ============================================================
# 1. LOAD DATA
# ============================================================
df = pd.read_csv("Salary_Data.csv")

# Make sure the expected columns exist
required_columns = ["YearsExperience", "Salary"]
missing = [col for col in required_columns if col not in df.columns]

if missing:
    raise ValueError(f"Missing columns in Salary_Data.csv: {missing}")

# ============================================================
# 2. APP CONFIGURATION
# ============================================================
app = Dash(__name__)
app.title = "Salary Analytics Dashboard"

# ============================================================
# 3. PROFESSIONAL STYLING
# ============================================================
COLORS = {
    "background": "#0B1120",
    "card": "#111827",
    "card_2": "#172033",
    "text": "#F8FAFC",
    "muted": "#94A3B8",
    "accent": "#38BDF8",
    "accent_2": "#8B5CF6",
    "success": "#22C55E",
    "border": "#263449",
    "grid": "#243044",
}

PLOT_LAYOUT = {
    "paper_bgcolor": COLORS["card"],
    "plot_bgcolor": COLORS["card"],
    "font": {"color": COLORS["text"], "family": "Arial"},
    "margin": {"l": 45, "r": 25, "t": 65, "b": 45},
    "xaxis": {
        "gridcolor": COLORS["grid"],
        "zerolinecolor": COLORS["grid"],
    },
    "yaxis": {
        "gridcolor": COLORS["grid"],
        "zerolinecolor": COLORS["grid"],
    },
}

# ============================================================
# 4. HELPER FUNCTIONS
# ============================================================
def card(title, value, subtitle, icon):
    return html.Div(
        [
            html.Div(
                [
                    html.Div(icon, className="kpi-icon"),
                    html.Div(
                        [
                            html.Div(title, className="kpi-title"),
                            html.Div(value, className="kpi-value"),
                            html.Div(subtitle, className="kpi-subtitle"),
                        ]
                    ),
                ],
                className="kpi-content",
            )
        ],
        className="kpi-card",
    )


def graph_card(title, description, graph_id):
    return html.Div(
        [
            html.Div(
                [
                    html.H3(title, className="chart-title"),
                    html.P(description, className="chart-description"),
                ],
                className="chart-header",
            ),
            dcc.Graph(
                id=graph_id,
                config={
                    "displayModeBar": True,
                    "displaylogo": False,
                    "responsive": True,
                },
            ),
        ],
        className="chart-card",
    )


# ============================================================
# 5. DASHBOARD LAYOUT
# ============================================================
app.layout = html.Div(
    [
        # ---------------- SIDEBAR ----------------
        html.Div(
            [
                html.Div(
                    [
                        html.Div("SA", className="brand-logo"),
                        html.Div(
                            [
                                html.Div("SALARY", className="brand-name"),
                                html.Div("ANALYTICS", className="brand-subtitle"),
                            ]
                        ),
                    ],
                    className="brand",
                ),

                html.Div(
                    [
                        html.Div("DASHBOARD", className="menu-label"),
                        html.Div("▦  Overview", className="menu-item active"),
                        html.Div("↗  Salary Analysis", className="menu-item"),
                        html.Div("◉  Experience Analysis", className="menu-item"),
                    ],
                    className="sidebar-menu",
                ),

                html.Div(
                    [
                        html.Div("DATASET", className="menu-label"),
                        html.Div(
                            [
                                html.Div("●", className="status-dot"),
                                html.Span("Salary_Data.csv"),
                            ],
                            className="dataset-status",
                        ),
                        html.Div(
                            f"{len(df):,} records loaded",
                            className="records-count",
                        ),
                    ],
                    className="sidebar-bottom",
                ),
            ],
            className="sidebar",
        ),

        # ---------------- MAIN CONTENT ----------------
        html.Div(
            [
                # Header
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div("BUSINESS INTELLIGENCE", className="eyebrow"),
                                html.H1(
                                    "Salary Analytics Dashboard",
                                    className="main-title",
                                ),
                                html.P(
                                    "Explore how professional experience impacts salary levels.",
                                    className="main-description",
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Div("●  LIVE DATA", className="live-badge"),
                                html.Div(
                                    "Interactive Analysis",
                                    className="header-small-text",
                                ),
                            ],
                            className="header-right",
                        ),
                    ],
                    className="top-header",
                ),

                # KPI Cards
                html.Div(
                    [
                        card(
                            "TOTAL RECORDS",
                            f"{len(df):,}",
                            "Employee records",
                            "▣",
                        ),
                        card(
                            "AVERAGE SALARY",
                            f"${df['Salary'].mean():,.0f}",
                            "Mean salary",
                            "$",
                        ),
                        card(
                            "HIGHEST SALARY",
                            f"${df['Salary'].max():,.0f}",
                            "Maximum recorded",
                            "↗",
                        ),
                        card(
                            "AVG. EXPERIENCE",
                            f"{df['YearsExperience'].mean():.1f} yrs",
                            "Average experience",
                            "◷",
                        ),
                    ],
                    className="kpi-grid",
                ),

                # Filters
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div("ANALYSIS FILTER", className="filter-label"),
                                html.Div(
                                    "Select the metric used for the distribution chart",
                                    className="filter-description",
                                ),
                            ]
                        ),
                        dcc.Dropdown(
                            id="metric-dropdown",
                            options=[
                                {
                                    "label": "Salary Distribution",
                                    "value": "Salary",
                                },
                                {
                                    "label": "Years of Experience",
                                    "value": "YearsExperience",
                                },
                            ],
                            value="Salary",
                            clearable=False,
                            className="custom-dropdown",
                        ),
                    ],
                    className="filter-bar",
                ),

                # Main Charts
                html.Div(
                    [
                        graph_card(
                            "Experience vs. Salary",
                            "Relationship between years of experience and salary",
                            "scatter-chart",
                        ),
                        graph_card(
                            "Salary Distribution",
                            "Distribution of salaries across all records",
                            "distribution-chart",
                        ),
                    ],
                    className="charts-row",
                ),

                html.Div(
                    [
                        graph_card(
                            "Salary by Experience",
                            "Salary progression for each experience level",
                            "bar-chart",
                        ),
                        graph_card(
                            "Salary Statistics",
                            "Key statistical summary of the salary dataset",
                            "box-chart",
                        ),
                    ],
                    className="charts-row",
                ),

                # Footer
                html.Div(
                    [
                        html.Span("Salary Analytics Dashboard"),
                        html.Span(" • "),
                        html.Span("Python • Dash • Plotly • Pandas"),
                    ],
                    className="footer",
                ),
            ],
            className="main-content",
        ),
    ]
)

# ============================================================
# 6. CALLBACKS
# ============================================================
@app.callback(
    Output("scatter-chart", "figure"),
    Output("distribution-chart", "figure"),
    Output("bar-chart", "figure"),
    Output("box-chart", "figure"),
    Input("metric-dropdown", "value"),
)
def update_dashboard(selected_metric):

    # -------- Scatter Plot --------
    scatter_fig = px.scatter(
        df,
        x="YearsExperience",
        y="Salary",
        trendline="ols",
        title="",
        labels={
            "YearsExperience": "Years of Experience",
            "Salary": "Salary ($)",
        },
        hover_data={
            "YearsExperience": ":.1f",
            "Salary": ":,.0f",
        },
    )

    scatter_fig.update_traces(
        marker=dict(
            size=10,
            line=dict(width=1),
        )
    )

    scatter_fig.update_layout(
        **PLOT_LAYOUT,
        xaxis_title="Years of Experience",
        yaxis_title="Salary ($)",
    )

    # -------- Distribution --------
    if selected_metric == "Salary":
        distribution_fig = px.histogram(
            df,
            x="Salary",
            nbins=10,
            title="",
            labels={"Salary": "Salary ($)"},
        )
        distribution_fig.update_layout(
            **PLOT_LAYOUT,
            xaxis_title="Salary ($)",
            yaxis_title="Number of Employees",
        )
    else:
        distribution_fig = px.histogram(
            df,
            x="YearsExperience",
            nbins=10,
            title="",
            labels={"YearsExperience": "Years of Experience"},
        )
        distribution_fig.update_layout(
            **PLOT_LAYOUT,
            xaxis_title="Years of Experience",
            yaxis_title="Number of Employees",
        )

    # -------- Bar Chart --------
    sorted_df = df.sort_values("YearsExperience")

    bar_fig = px.bar(
        sorted_df,
        x="YearsExperience",
        y="Salary",
        title="",
        labels={
            "YearsExperience": "Years of Experience",
            "Salary": "Salary ($)",
        },
    )

    bar_fig.update_layout(
        **PLOT_LAYOUT,
        xaxis_title="Years of Experience",
        yaxis_title="Salary ($)",
    )

    # -------- Box Plot --------
    box_fig = go.Figure()

    box_fig.add_trace(
        go.Box(
            y=df["Salary"],
            name="Salary",
            boxpoints="all",
            jitter=0.35,
            pointpos=0,
            hovertemplate="Salary: $%{y:,.0f}<extra></extra>",
        )
    )

    box_fig.update_layout(
        **PLOT_LAYOUT,
        yaxis_title="Salary ($)",
        xaxis_title="",
        showlegend=False,
    )

    return scatter_fig, distribution_fig, bar_fig, box_fig


# ============================================================
# 7. RUN APPLICATION
# ============================================================
if __name__ == "__main__":
    app.run(debug=True, port=8051)
