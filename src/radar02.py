#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 12:44:20 2023

@author: eduardo
"""

import plotly.graph_objects as go
import plotly.offline as pyo

import pandas as pd

import argparse
import sys


def parse_arguments(args):
    parser = argparse.ArgumentParser(description='Parse CSV to radar plot')
    parser.add_argument('input_file',  type=argparse.FileType('r'),
                        help='Data File')
    parser.add_argument(
        '--fill', default=None, choices=['toself', 'tonext', None])
    parser.add_argument('--title', default=None)
    parser.add_argument('--output_file', default=None)
    parser.add_argument('--show_legend', action='store_true')
    parser.add_argument('--show_radialaxis', action='store_true')
    return parser.parse_args(args)


def main(args):
    opt = parse_arguments(args)
    df = pd.read_csv(opt.input_file, index_col=0)
    categories = [*df.columns[1:], df.columns[1]]

    data = [go.Scatterpolar(
                r=[*row.values, row.values[0]],
                theta=categories,
                fill=opt.fill,
                name=label) for label, row in df.iterrows()]

    fig = go.Figure(
        data=data,
        layout=go.Layout(
            title=go.layout.Title(text=opt.title, xanchor='center', x=0.5),
            polar={'radialaxis': {'visible': opt.show_radialaxis}},
            showlegend=opt.show_legend
        )
    )
    if opt.output_file:
        fig.write_image(opt.output_file)
    else:
        pyo.plot(fig)

if __name__ == "__main__":
    main(sys.argv[1:])