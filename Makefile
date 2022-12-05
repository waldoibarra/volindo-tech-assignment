service_name = "volindo-tech-assignment"

help: ## Print help for each target.
	$(info Available commands:)
	$(info )
	@grep '^[[:alnum:]_-]*:.* ##' $(MAKEFILE_LIST) \
		| sort | awk 'BEGIN {FS=":.* ## "}; {printf "%-25s %s\n", $$1, $$2};'

part-1: rebuild ## Run the part 1 of the assignment.
	docker compose run --rm $(service_name) part-1

part-2: rebuild ## Run the part 2 of the assignment.
	docker compose run --rm $(service_name) part-2

debug: rebuild ## To get in the container and see what's going on.
	docker compose run --rm --entrypoint bash $(service_name)

rebuild:
	docker compose build
