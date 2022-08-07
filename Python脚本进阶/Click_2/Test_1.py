#*****************************#
#                             #
#**** 课时2：Click 使用     ****#
# --1--                       #
#                             #
#*****************************#
# Click 快速开始




import click


@click.command()

#定义参数
# @click.argument( 'count', type=int)
@click.argument( 'count', type=str)
@click.option('--ocount', type=int, default=1)
def hello(count, ocount):
    click.echo(count)
    click.echo(ocount)
    click.echo("Hello, World! --1 ")
if __name__ == '__main__':
    hello();

