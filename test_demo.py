from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "dyj",
    "start_date": datetime(2026,10,19),
}

with DAG(
    dag_id="test_demo",
    default_args=default_args,
    schedule_interval="*/5 * * * *",  # cron：每5分钟自动执行一次
    catchup=False,  # 关闭补跑，不会一次性执行过去时间的任务
    description="Airflow测试Demo，打印hello",
) as dag:
    # 任务1：输出hello
    task_hello = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello Airflow! 测试任务执行成功'",
    )

    # 任务2：查看系统时间
    task_date = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    # 设置依赖：先执行task_hello，成功之后才跑task_date
    task_hello >> task_date
