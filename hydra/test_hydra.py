
import hydra
from hydra import utils

@hydra.main(config_path="conf", config_name="default")
def app(cfg):
    print(cfg.project.name, cfg.project.exp_name)
    print(cfg.pretty(resolve=True)) 

if __name__ == "__main__":
    app()
