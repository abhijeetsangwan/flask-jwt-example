

To RUN

1. Run server
	python demo.py

2. Run CURL to get auth token
	curl 	-i \
		-H "Content-Type: application/json" \
		-H "Accept: application/json" \
		-X POST \
		-d '{"username": "user1", "password": "pass1"}' \
		http://localhost:10001/authorize-me

3. Run Another CURL to access protected end point using token from previous run

	curl 	-i \
		-H "Authorization: JWT <insert_token_here>" \
		-H "Content-Type: application/json" \
		-H "Accept: application/json" \
		-X POST  \
		http://localhost:10001/protected	


