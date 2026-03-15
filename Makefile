install:
	uv sync

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games

format:
	uv run ruff format brain_games

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl
