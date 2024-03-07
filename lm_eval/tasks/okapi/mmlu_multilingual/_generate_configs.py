import datasets
import yaml
from tqdm import tqdm


def main() -> None:
    dataset_path = "alexandrainst/m_mmlu"

    for task in tqdm(datasets.get_dataset_infos(dataset_path).keys()):
        file_name = f"m_mmlu_{task}.yaml"
        try:
            with open(f"{file_name}", "w") as f:
                f.write("# Generated by _generate_configs.py\n")
                yaml.dump(
                    {
                        "include": "_default_yaml",
                        "task": f"{dataset_path.split('/')[-1]}_{task}",
                        "dataset_name": task,
                    },
                    f,
                )
        except FileExistsError:
            pass


if __name__ == "__main__":
    main()
