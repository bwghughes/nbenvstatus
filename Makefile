start:
	export PAGE_NAME="Nedbank E2E" && \
	export ENVSTATUS_DB_URL="sqlite:///envstatus.db" && \
	apistar create_tables && \
	apistar run

test:
	export ENVSTATUS_DB_URL=sqlite:///test.db && \
	apistar create_tables && \
	py.test --cov=project --cov-report=term-missing project tests.py && \
	rm -f test.db

envcheck:
	export ENVSTATUS_BASE_URL=http://127.0.0.1:8080 && \
	py.test environment_tests.py

clean:
	rm *.db

