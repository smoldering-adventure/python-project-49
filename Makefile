install:
	uv sync

brain_games:
	uv run brain_games

brain_even:
	uv run brain_even

brain_calc:
	uv run brain_calc

brain_gcd:
	uv run brain_gcd

brain_progression:
	uv run brain_progression

brain_prime:
	uv run brain_prime

build:
	uv build

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report 

lint:
	uv run ruff check brain_games

check: test lint

.PHONY: install test lint selfcheck check build