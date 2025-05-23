import dash
from dash import dcc, html
from repository.biDashboardRepository import BiDashboardRepository
from .figures.stockFigure import stockFigure
from .figures.loanFigure import LoanFigure
from .figures.GasIncomesFigure import GasIncomesFigure
from .figures.IncomeFigure import IncomeProfit
from .figures.ManagerTransactionFigure import GetManagerTransactionFigure
from .figures.EmptySellingIncomeFigure import EmptySellingIncomeFigure
from .figures.VehicleTransactionFigure import VehicleTransactionFigure
from .figures.UnFinishedLoanBalanceFigure import UnFinishedLoanBalanceFigure
from .figures.CylinderSellCountFigure import CylinderSellCountFigure
from .figures.reg_and_unregFigure import RegAndUnregCustomerCountsFigure
from .figures.CylinderCountFigure import displayCylinderCountCard
from .figures.cardFigure import displayincome

# Enhanced Litro Gas Dashboard Layout with modern white styling

def mainLayout(repo: BiDashboardRepository):
    return html.Div(
        className="dashboard-container",
        style={
            'minHeight': '100vh',
            'margin': '0',
            'padding': '0',
            'backgroundColor': '#f8fafc'
        },
        children=[
            # Header Section
            html.Div(
                className="header-section",
                style={
                    'background': 'linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%)',
                    'boxShadow': '0 4px 20px rgba(0,0,0,0.08)',
                    'borderRadius': '16px',
                    'margin': '20px',
                    'padding': '40px',
                    'textAlign': 'center',
                    'border': '1px solid rgba(0,0,0,0.06)'
                },
                children=[
                    html.H1(
                        "Litro Gas Business Intelligence", 
                        style={
                            'color': '#1e293b',
                            'fontSize': '3rem',
                            'fontWeight': '700',
                            'margin': '0',
                            'fontFamily': "'Inter', sans-serif",
                            'letterSpacing': '-0.02em'
                        }
                    ),
                    html.P(
                        "Real-time Analytics & Performance Dashboard", 
                        style={
                            'color': '#64748b',
                            'fontSize': '1.1rem',
                            'fontWeight': '400',
                            'marginTop': '10px',
                            'fontFamily': "'Inter', sans-serif"
                        }
                    )
                ]
            ),

            # Key Metrics Row (Top two value cards)
            html.Div(
                style={
                    'display': 'grid',
                    'gridTemplateColumns': 'repeat(auto-fit, minmax(300px, 1fr))',
                    'gap': '20px',
                    'padding': '0 20px',
                    'marginBottom': '30px'
                },
                children=[
                    html.Div(
                        className="metric-card",
                        style={
                            'background': 'linear-gradient(135deg, #ffffff 0%, #f8fafc 100%)',
                            'border': '2px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '30px',
                            'textAlign': 'center',
                            'boxShadow': '0 8px 25px rgba(0,0,0,0.08)',
                            'transition': 'all 0.3s ease',
                            'position': 'relative',
                            'overflow': 'hidden'
                        },
                        children=[
                            html.Div(
                                style={
                                    'fontSize': '1rem',
                                    'color': '#64748b',
                                    'fontWeight': '500',
                                    'marginBottom': '15px',
                                    'textTransform': 'uppercase',
                                    'letterSpacing': '0.5px'
                                },
                                children="📊 Cylinder Inventory Count"
                            ),
                            html.Div(
                                style={
                                    'fontSize': '3rem',
                                    'fontWeight': '700',
                                    'color': '#1e293b',
                                    'lineHeight': '1',
                                    'fontFamily': "'Inter', sans-serif"
                                },
                                children=f"{repo.getCylinderCountFromUserToGiveUs()}"
                            )
                        ]
                    ),

                    html.Div(
                        className="metric-card",
                        style={
                            'background': 'linear-gradient(135deg, #ffffff 0%, #f8fafc 100%)',
                            'border': '2px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '30px',
                            'textAlign': 'center',
                            'boxShadow': '0 8px 25px rgba(0,0,0,0.08)',
                            'transition': 'all 0.3s ease',
                            'position': 'relative',
                            'overflow': 'hidden'
                        },
                        children=[
                            html.Div(
                                style={
                                    'fontSize': '1rem',
                                    'color': '#64748b',
                                    'fontWeight': '500',
                                    'marginBottom': '15px',
                                    'textTransform': 'uppercase',
                                    'letterSpacing': '0.5px'
                                },
                                children="💰 Active Loan Accounts"
                            ),
                            html.Div(
                                style={
                                    'fontSize': '3rem',
                                    'fontWeight': '700',
                                    'color': '#1e293b',
                                    'lineHeight': '1',
                                    'fontFamily': "'Inter', sans-serif"
                                },
                                children=f"{repo.getActiveLoanAcount()}"
                            )
                        ]
                    ),
                ]
            ),
            
            # Main Grid Container for Charts
            html.Div(
                style={
                    'display': 'grid',
                    'gridTemplateColumns': 'repeat(auto-fit, minmax(600px, 1fr))',
                    'gap': '25px',
                    'padding': '0 20px 40px 20px',
                    'maxWidth': '1800px',
                    'margin': '0 auto'
                },
                children=[
                    # Analytics Cards
                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "📈 Monthly Gas Comparison", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=stockFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "🏦 Loan Management", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=LoanFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "⛽ Gas Income Analytics", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=GasIncomesFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "💎 Total Profit Analysis", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=IncomeProfit(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "👨‍💼 Manager Transactions", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=GetManagerTransactionFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "🔄 Empty Cylinder Sales", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=EmptySellingIncomeFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "🚛 Vehicle Transactions", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=VehicleTransactionFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "⚠️ Outstanding Loan Balance", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=UnFinishedLoanBalanceFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "📦 Cylinder Sales Volume", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=CylinderSellCountFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),

                    html.Div(
                        className="chart-card",
                        style={
                            'background': '#ffffff',
                            'border': '1px solid #e2e8f0',
                            'borderRadius': '16px',
                            'padding': '25px',
                            'boxShadow': '0 4px 15px rgba(0,0,0,0.05)',
                            'transition': 'all 0.3s ease'
                        },
                        children=[
                            html.H2(
                                "👥 Customer Registration Stats", 
                                style={
                                    'color': '#1e293b',
                                    'fontSize': '1.3rem',
                                    'fontWeight': '600',
                                    'margin': '0 0 20px 0',
                                    'paddingBottom': '12px',
                                    'borderBottom': '2px solid #f1f5f9',
                                    'fontFamily': "'Inter', sans-serif"
                                }
                            ),
                            dcc.Graph(
                                figure=RegAndUnregCustomerCountsFigure(repository=repo),
                                config={'displayModeBar': True, 'responsive': True}
                            ),
                        ]
                    ),
                ]
            )
        ]
    )