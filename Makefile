start:
	export ENVSTATUS_DB_URL=sqlite:///envstatus.db && apistar run

seed:
	rm envstatus.db && \
	export ENVSTATUS_DB_URL=sqlite:///envstatus.db && \
	apistar create_tables && \
	apistar create_environments

test:
	export ENVSTATUS_DB_URL=sqlite:///envstatus-test.db && \
	apistar create_tables && \
	apistar create_environments && \
	apistar test && \
	rm envstatus-test.db