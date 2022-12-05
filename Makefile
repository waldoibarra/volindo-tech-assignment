help: ## Print help for each target.
	$(info Available commands:)
	$(info )
	@grep '^[[:alnum:]_-]*:.* ##' $(MAKEFILE_LIST) \
		| sort | awk 'BEGIN {FS=":.* ## "}; {printf "%-25s %s\n", $$1, $$2};'

part-1: rebuild ## Run the part 1 of the challenge.
	docker compose run --rm volindo-tech-assignment part-1

debug: rebuild ## To get in the container and see what's going on.
	docker compose run --rm --entrypoint bash volindo-tech-assignment

rebuild:
	docker compose build
