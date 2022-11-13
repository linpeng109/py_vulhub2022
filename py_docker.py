import random
import docker

from py_config import ConfigFactory
from py_logging import LoggerFactory 


class DockerController():
    def __init__(self, config, logger) -> None:
        self.config = config
        self.logger = logger

    def get_docker_client(self):
        docker_client = docker.DockerClient(
            base_url='unix://var/run/docker.sock')
        return docker_client

    # 关闭所有已经运行的container
    def close_all_docker_cntainer(self, docker_client):
        docker_running_container_list = docker_client.containers.list()
        for running_container in docker_running_container_list:
            docker_client.containers.stop(running_container.id)

    # 启动一个container
    def start_docker_container(self, docker_client, docker_container_id=''):

        # 从配置文件中获取对应表
        script_list = []
        keyword_scripts = self.config.items('keyword_script')
        for script, keyword in keyword_scripts:
            script_list.append(script)

        # 随机选择脚本
        size = len(script_list)
        selected_script = script_list[random.randint(0, size-1)]
        print(selected_script)

        # 启动选择脚本相关的所有容器
        docker_container_list = docker_client.containers.list(all=True)
        print(len(docker_container_list))
        container_selected_list = []
        for container in docker_container_list:
            if selected_script in container.name:
                print("{id=%s;name=%s}" % (container.id[0:4], container.name))
                container_selected_list.append(container.id)
        return container_selected_list


if __name__ == '__main__':
    config = ConfigFactory(config_file='py_robot202.ini').get_config()
    logger = LoggerFactory(config_factory=config).get_logger()

    docker_controller = DockerController(config=config, logger=logger)
    docker_client = docker_controller.get_docker_client()
    container_selected_list = docker_controller.start_docker_container(
        docker_client=docker_client)
