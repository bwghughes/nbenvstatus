start:
	export ENVSTATUS_DB_URL="sqlite:///envstatus.db" && \
	apistar create_tables && \
	apistar create_envs && \
	apistar run

test:
	export ENVSTATUS_DB_URL=sqlite:///test.db && \
	apistar create_tables && \
	apistar create_envs && \
	py.test --cov=project tests.py && \
	rm -f test.db