from searchtweets import ResultStream, gen_rule_payload, load_credentials
from searchtweets import collect_results


enterprise_search_args = load_credentials("twitter_keys.yaml",
                                          yaml_key="search_tweets_enterprise",
                                          env_overwrite=False)


rule = gen_rule_payload("atlantis", results_per_call=100) # testing with a sandbox account
print(rule)

tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=enterprise_search_args) # change this if you need to