import java.util.Scanner;
import java.util.Random;

public class MineSweeper {
    // 地图尺寸
    static final int ROW = 10;
    static final int COL = 10;
    // 地雷数量
    static final int MINE_NUM = 12;
    // 游戏地图 0空白 1-8数字 9地雷
    static int[][] map = new int[ROW][COL];
    // 显示面板
    static char[][] show = new char[ROW][COL];
    // 是否标记地雷
    static boolean[][] flag = new boolean[ROW][COL];
    static Scanner sc = new Scanner(System.in);
    static Random ran = new Random();
    static boolean gameOver = false;

    public static void main(String[] args) {
        initGame();
        while (!gameOver) {
            printMap();
            System.out.println("1:翻开格子  2:插旗标记地雷");
            System.out.print("请输入操作类型：");
            int op = sc.nextInt();
            System.out.print("输入行 列(空格隔开)：");
            int r = sc.nextInt() - 1;
            int c = sc.nextInt() - 1;

            if (!checkPos(r, c)) {
                System.out.println("坐标超出范围！");
                continue;
            }

            if (op == 1) {
                openBlock(r, c);
            } else if (op == 2) {
                setFlag(r, c);
            }
            checkWin();
        }
    }

    // 初始化游戏
    static void initGame() {
        // 初始化显示面板全为#
        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                show[i][j] = '#';
                flag[i][j] = false;
            }
        }
        // 布置地雷
        putMine();
        // 计算周围地雷数
        countMine();
    }

    // 随机放地雷
    static void putMine() {
        int count = 0;
        while (count < MINE_NUM) {
            int x = ran.nextInt(ROW);
            int y = ran.nextInt(COL);
            if (map[x][y] != 9) {
                map[x][y] = 9;
                count++;
            }
        }
    }

    // 统计每个格子周围地雷数
    static void countMine() {
        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (map[i][j] == 9) continue;
                int num = 0;
                // 遍历8个方向
                for (int dr = -1; dr <= 1; dr++) {
                    for (int dc = -1; dc <= 1; dc++) {
                        int nr = i + dr;
                        int nc = j + dc;
                        if (checkPos(nr, nc) && map[nr][nc] == 9) {
                            num++;
                        }
                    }
                }
                map[i][j] = num;
            }
        }
    }

    // 翻开格子
    static void openBlock(int r, int c) {
        if (show[r][c] != '#' || flag[r][c]) return;
        // 踩到地雷
        if (map[r][c] == 9) {
            System.out.println("踩到地雷！游戏结束！");
            showAllMine();
            gameOver = true;
            return;
        }
        // 显示数字
        show[r][c] = (char) (map[r][c] + '0');
        // 空白格自动扩散翻开
        if (map[r][c] == 0) {
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    int nr = r + dr;
                    int nc = c + dc;
                    openBlock(nr, nc);
                }
            }
        }
    }

    // 插旗标记地雷
    static void setFlag(int r, int c) {
        if (show[r][c] != '#') return;
        flag[r][c] = !flag[r][c];
        show[r][c] = flag[r][c] ? 'F' : '#';
    }

    // 打印地图
    static void printMap() {
        System.out.print("  ");
        for (int i = 1; i <= COL; i++) System.out.print(i + " ");
        System.out.println();
        for (int i = 0; i < ROW; i++) {
            System.out.print((i + 1) + " ");
            for (int j = 0; j < COL; j++) {
                System.out.print(show[i][j] + " ");
            }
            System.out.println();
        }
    }

    // 判定坐标合法
    static boolean checkPos(int r, int c) {
        return r >= 0 && r < ROW && c >= 0 && c < COL;
    }

    // 胜利判定
    static void checkWin() {
        int empty = 0;
        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (show[i][j] == '#') empty++;
            }
        }
        if (empty == MINE_NUM) {
            System.out.println("恭喜你！扫雷成功通关！");
            gameOver = true;
        }
    }

    // 结束展示全部地雷
    static void showAllMine() {
        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (map[i][j] == 9) show[i][j] = '*';
            }
        }
        printMap();
    }
}

