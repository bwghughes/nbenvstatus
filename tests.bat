SET ENVSTATUS_DB_URL=sqlite:///test.db && 
apistar create_tables && 
apistar create_envs && 
py.test --cov=project project tests.py && 
del test.db