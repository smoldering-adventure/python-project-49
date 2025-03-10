install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

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

lint:
	uv run ruff check brain_games
