#*****************************#
#                             #
#**** 课时2：Click 使用     ****#
# --2-                       #
#                             #
#*****************************#
# Click 快速开始




import click


@click.command()

#获取用户输入 Prompt

def hello():
    count = click.prompt("pelae input a int", type=int)
    click.echo(count)
    click.echo("Hello, World! --2 ")
    if click.confirm("do you want to continue"):
        click.echo("done")

if __name__ == '__main__':
    hello()

