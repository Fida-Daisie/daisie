from dash import  html

import dash_bootstrap_components as dbc
class Helper():


    @staticmethod
    def help_button(id, popover_header=None, popover_body=None, title=None):
        return [
            html.Div(
            html.Button(
                html.I(className="fa fa-info"),
                id=id+"-popover-button",
                title=title,
                className="btn-help-inner"
            ),
            className="btn-help-outer"),

            dbc.Popover(
                children=[
                    dbc.PopoverHeader(popover_header),
                    dbc.PopoverBody(popover_body, id=id+"-data-source")
                ],
                id=id+"-popover",
                trigger="legacy",
                target=id+"-popover-button",
                placement="auto"
            )
        ]
