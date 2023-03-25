import time

from collections import Counter
import leetcode
import leetcode.auth

def start_leetcode(leetcode_session, csrf_token):
  csrf_token = leetcode.auth.get_csrf_cookie(leetcode_session)

  configuration = leetcode.Configuration()

  configuration.api_key["x-csrftoken"] = csrf_token
  configuration.api_key["csrftoken"] = csrf_token
  configuration.api_key["LEETCODE_SESSION"] = leetcode_session
  configuration.api_key["Referer"] = "https://leetcode.com"
  configuration.debug = False

  return leetcode.DefaultApi(leetcode.ApiClient(configuration))

def test_leetcode():
  graphql_request = leetcode.GraphqlQuery(
    query="""
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            boundTopicId
            title
            content
            translatedTitle
            isPaidOnly
            difficulty
            likes
            dislikes
            isLiked
            similarQuestions
            contributors {
              username
              profileUrl
              avatarUrl
              __typename
            }
            langToValidPlayground
            topicTags {
              name
              slug
              translatedName
              __typename
            }
            companyTagStats
            codeSnippets {
              lang
              langSlug
              code
              __typename
            }
            stats
            codeDefinition
            hints
            solution {
              id
              canSeeDetail
              __typename
            }
            status
            sampleTestCase
            enableRunCode
            metaData
            translatedContent
            judgerAvailable
            judgeType
            mysqlSchemas
            enableTestMode
            envInfo
            __typename
          }
        }
    """,
    variables=leetcode.GraphqlQueryGetQuestionDetailVariables(topic_slug='tree'),
    operation_name="getQuestionDetail",
  )

  print(api_instance.graphql_post(body=graphql_request))

def killme(api_instance):
  return api_instance.api_problems_topic_get(topic="algorithms")

api_instance = start_leetcode("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb2NpYWxhY2NvdW50X3NvY2lhbGxvZ2luIjp7ImFjY291bnQiOnsiaWQiOm51bGwsInVzZXJfaWQiOm51bGwsInByb3ZpZGVyIjoiZ29vZ2xlIiwidWlkIjoiMTA5NDQ1NjkzMTY2NzExNTk0MjcyIiwibGFzdF9sb2dpbiI6bnVsbCwiZGF0ZV9qb2luZWQiOm51bGwsImV4dHJhX2RhdGEiOnsiaWQiOiIxMDk0NDU2OTMxNjY3MTE1OTQyNzIiLCJlbWFpbCI6ImhpdGVjaC50ZWNoMTAxQGdtYWlsLmNvbSIsInZlcmlmaWVkX2VtYWlsIjp0cnVlLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FDQi1SNVJoUDAtNFpRYnlOR0xwVWVRc0JaelJUM0hkeU43UWJmbDE1Skk1MUE9czk2LWMifX0sInVzZXIiOnsiaWQiOm51bGwsInBhc3N3b3JkIjoiIUYwNWt5WkZDRDZuODFwclV6aXlIWXoyRWJWaFR5MUZDOVVQb01zYzMiLCJsYXN0X2xvZ2luIjpudWxsLCJpc19zdXBlcnVzZXIiOmZhbHNlLCJ1c2VybmFtZSI6IiIsImZpcnN0X25hbWUiOiIiLCJsYXN0X25hbWUiOiIiLCJlbWFpbCI6ImhpdGVjaC50ZWNoMTAxQGdtYWlsLmNvbSIsImlzX3N0YWZmIjpmYWxzZSwiaXNfYWN0aXZlIjp0cnVlLCJkYXRlX2pvaW5lZCI6IjIwMjMtMDMtMjFUMjE6MTE6MzguNzE4WiJ9LCJzdGF0ZSI6eyJuZXh0IjoiLyIsInByb2Nlc3MiOiJsb2dpbiIsInNjb3BlIjoiIiwiYXV0aF9wYXJhbXMiOiIifSwiZW1haWxfYWRkcmVzc2VzIjpbeyJpZCI6bnVsbCwidXNlcl9pZCI6bnVsbCwiZW1haWwiOiJoaXRlY2gudGVjaDEwMUBnbWFpbC5jb20iLCJ2ZXJpZmllZCI6dHJ1ZSwicHJpbWFyeSI6dHJ1ZX1dLCJ0b2tlbiI6eyJpZCI6bnVsbCwiYXBwX2lkIjoxLCJhY2NvdW50X2lkIjpudWxsLCJ0b2tlbiI6InlhMjkuYTBBVnZaVnNwTVdjWm5SeHZkQTRMOExiSjlZMHNYMTBiWnA3REZPcFYwV1haX2g0LU9GcWVoaWJZY3d0LVNFRVhCcldVSFpUSC10TlVOTkRtMXNpMkNTM1lZNDllOHA5dy11cGM2b2drMlV0Z1Y2MVVnZVhvMC1xMGl0Qld6R1pwN3BnR3R1eGJzeTNkYjFvSEE5UlFFSUxMdkdOR2lzZ01hQ2dZS0FaWVNBUklTRlFHYmR3YUlCMWpzdG10ckFtUUpfWUJyOS1ZNnlnMDE2NiIsInRva2VuX3NlY3JldCI6IiIsImV4cGlyZXNfYXQiOiIyMDIzLTAzLTIxVDIyOjExOjM3LjU4OFoifX0sIl9hdXRoX3VzZXJfaWQiOiI0MDE0MjcwIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDJiNDBiMDE0OTA1ZWUwNjhiYzk1ODIxOGRjODIxZjhmNzg2MGQ2NiIsImlkIjo0MDE0MjcwLCJlbWFpbCI6ImhpdGVjaC50ZWNoMTAxQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiQ29tcFNjaUdvZCIsInVzZXJfc2x1ZyI6IkNvbXBTY2lHb2QiLCJhdmF0YXIiOiJodHRwczovL3MzLXVzLXdlc3QtMS5hbWF6b25hd3MuY29tL3MzLWxjLXVwbG9hZC9hc3NldHMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNjc5NzY1OTg0LCJpcCI6IjEyOC42LjM3LjcwIiwiaWRlbnRpdHkiOiJjM2ZjZDllNTJmZDc3NWM0M2M5NTUzYTk2MWJmYzUyYyIsInNlc3Npb25faWQiOjM2OTUwNjQ1LCJfc2Vzc2lvbl9leHBpcnkiOjEyMDk2MDB9.GWBiaeq5xhbawMaZo9WVCvOF_ZQg3Gk8_1tikTkAm5M","N91ZBKL5Rm2n9kgHQCi0siu6Ip6sGD5C2LJ5gFpsdIfMQ0Ag6OBTY2CuogUGNtxl")

test_leetcode()


