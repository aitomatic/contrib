"""H1st CLI."""


import click

from .pmfp import h1st_pmfp_cli


@click.group(name='h1st',
             cls=click.Group,
             commands={},
             invoke_without_command=False,
             no_args_is_help=True,
             subcommand_metavar='H1ST_SUB_COMMAND',
             chain=False,
             help='H1st CLI >>>',
             epilog='^^^ H1st CLI',
             short_help='H1st CLI',
             options_metavar='[OPTIONS]',
             add_help_option=True,
             hidden=False,
             deprecated=False)
def h1st_cli():
    """Trigger H1st from CLI."""
