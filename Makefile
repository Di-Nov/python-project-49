install:
	poetry install

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-even:
	poetry run brain-even

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

publish:
	poetry publish --dry-run

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
