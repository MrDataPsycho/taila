from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


# Optional default env path
ENV_PATH = Path(".envs").joinpath("dev.env")


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    HF_TOKEN: str
    LLAMAPARSE_API_TOKEN: str

    model_config = SettingsConfigDict(
        env_file=ENV_PATH if ENV_PATH.exists() else None,
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )

    @classmethod
    def from_env_file(cls, env_path: str | Path) -> "Settings":
        env_path = Path(env_path)
        if not env_path.exists():
            raise FileNotFoundError(f"Env file {env_path} does not exist.")

        # Dynamically create a subclass with overridden model_config
        class CustomSettings(cls):
            model_config = SettingsConfigDict(
                env_file=env_path,
                env_file_encoding="utf-8",
                extra="ignore",
                case_sensitive=False
            )

        return CustomSettings()


if __name__ == "__main__":
    settings = Settings()
    print(settings)
