import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class MazeSolver extends JFrame {
    private int[][] maze;
    private int n;
    private JPanel[][] cellPanels;
    private Point[][] backtrack;

    public MazeSolver(int[][] maze) {
        this.maze = maze;
        this.n = maze.length;
        this.cellPanels = new JPanel[n][n];
        this.backtrack = new Point[n][n];

        initializeUI();
    }

    private void initializeUI() {
        setTitle("Maze Solver");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cellPanels[i][j] = new JPanel();
                cellPanels[i][j].setBackground(getColorForCell(maze[i][j]));

                gbc.gridx = j;
                gbc.gridy = i;
                gbc.weightx = 1.0;
                gbc.fill = GridBagConstraints.BOTH;
                add(cellPanels[i][j], gbc);
            }
        }

        JButton solveButton = new JButton("Solve");
        solveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                solveMaze();
            }
        });

        gbc.gridx = 0;
        gbc.gridy = n;
        gbc.weightx = 1.0;
        gbc.gridwidth = n;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.anchor = GridBagConstraints.PAGE_END;
        gbc.insets = new Insets(10, 0, 0, 0);
        add(solveButton, gbc);

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private Color getColorForCell(int cellValue) {
        if (cellValue == 0) {
            return Color.WHITE;
        } else if (cellValue == 1) {
            return Color.BLACK;
        } else if (cellValue == 2) {
            return Color.GREEN;
        } else if (cellValue == 3) {
            return Color.BLUE;
        }
        return Color.WHITE;
    }

    private void solveMaze() {
        int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
        boolean[][] visited = new boolean[n][n];
        Queue<Point> queue = new LinkedList<>();

        queue.offer(new Point(0, 0));
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            Point current = queue.poll();
            int x = current.x;
            int y = current.y;

            if (maze[x][y] == 2) {
                reconstructPath(current);
                break;
            }

            for (int[] dir : directions) {
                int newX = x + dir[0];
                int newY = y + dir[1];

                if (newX >= 0 && newX < n && newY >= 0 && newY < n && !visited[newX][newY] && maze[newX][newY] != 1) {
                    visited[newX][newY] = true;
                    queue.offer(new Point(newX, newY));
                    backtrack[newX][newY] = new Point(x, y);
                }
            }
        }
    }

    private void reconstructPath(Point end) {
        while (end != null) {
            maze[end.x][end.y] = 3;
            cellPanels[end.x][end.y].setBackground(getColorForCell(3));
            end = backtrack[end.x][end.y];
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the maze: ");
        int n = scanner.nextInt();
        int[][] mazeData = new int[n][n];
        System.out.println("Enter the maze values (0: path, 1: wall, 2: start/end):");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mazeData[i][j] = scanner.nextInt();
            }
        }

        scanner.close();

        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new MazeSolver(mazeData);
            }
        });
    }
}
