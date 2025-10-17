run:
	uv run uvicorn app.main:app --reload

format:
	uv run ruff format .

lint:
	uv run ruff check .

test:
	uv run python test.py