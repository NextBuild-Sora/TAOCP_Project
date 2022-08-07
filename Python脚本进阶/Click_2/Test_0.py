#*****************************#
#                             #
#**** 课时2：Click 使用     ****#
# --0--                       #
#                             #
#*****************************#
# Click 快速开始



import click

@click.command()

#定义可选选项 Option
@click.option('--count', default=1, type=int, help="your count" )
def hello(count):
    click.echo(count)
    click.echo("Hello World!")
if __name__ == '__main__':
    hello()

