import time

from collections import Counter


topic_to_accepted = Counter()
topic_to_total = Counter()


# Take only the first 10 for test purposes
for slug in list(slug_to_solved_status.keys())[:10]:
    time.sleep(1)  # Leetcode has a rate limiter
    
    graphql_request = leetcode.GraphqlQuery(
        query="""
            query getQuestionDetail($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                topicTags {
                  name
                  slug
                }
              }
            }
        """,
        variables=leetcode.GraphqlQueryVariables(title_slug=slug),
        operation_name="getQuestionDetail",
    )

    api_response = api_instance.graphql_post(body=graphql_request)
    
    for topic in (tag.slug for tag in api_response.data.question.topic_tags):
        topic_to_accepted[topic] += int(slug_to_solved_status[slug])
        topic_to_total[topic] += 1

print(
    list(
        sorted(
            ((topic, accepted / topic_to_total[topic]) for topic, accepted in topic_to_accepted.items()),
            key=lambda x: x[1]
        )
    )
)