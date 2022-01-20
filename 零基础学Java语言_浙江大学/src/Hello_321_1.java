
/*
 *	第3周 循环.
 *	3.2 循环的例子.
 *	3.2.1_1 计数循环.
 */

public class Hello_321_1 {
    public static void main(String[] args) {

        int count = 10;
//        先进循环体
        do {
            System.out.println(count);
            count = count - 1;
        }
//        循环条件
        while (count > 0);
        System.out.println("发射");
        System.out.println("循环结束后："+count);
    }
}
