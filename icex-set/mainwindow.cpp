#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>
#include <QTextStream>
#include <QFile>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    str_dir_set = (QDir::homePath()+"/.icewm");

    if (!QDir(str_dir_set).exists())
    {
        QDir dir;
        dir.mkdir(str_dir_set);
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_Exit_clicked()
{
    close();
}

void MainWindow::on_pushButton_DesktopImage_clicked()
{
    QString str = QFileDialog::getOpenFileName(0, "Open Dialog", "/usr/share/wallpapers", "*.jpg *.jpeg *.png");
    ui->DesktopImage->setText(str);
}

void MainWindow::on_pushButton_SaveApp_clicked()
{
    QString str_check;

    str_file_set = str_dir_set + "/prefoverride";
    QFile fileSet(str_file_set);
    fileSet.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream writeStream(&fileSet);
    if (ui->DesktopImage->text() != "")
        {
            QString str_des;
            str_des = "DesktopBackgroundImage=" + ui->DesktopImage->text() + "\n";
            writeStream << str_des;
        }


    if (ui->checkBox_DesktopCentr->checkState())
    {
        str_check = "DesktopBackgroundCenter=1";
    }
    else
    {
        str_check = "DesktopBackgroundCenter=0";
    }
    writeStream << str_check + "\n";

    if (ui->checkBox_DesktopScaled->checkState())
    {
        str_check = "DesktopBackgroundScaled=1";
    }
    else
    {
        str_check = "DesktopBackgroundScaled=0";
    }
    writeStream << str_check + "\n";

    fileSet.close();

    char *prog = "icewmbg -r";
    system(prog);

}
