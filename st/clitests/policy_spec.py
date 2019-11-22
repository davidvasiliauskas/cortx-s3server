import os
import yaml
import json
from framework import Config
from framework import S3PyCliTest
from awss3api import AwsTest
from s3cmd import S3cmdTest
from s3client_config import S3ClientConfig
from aclvalidation import AclTest
from auth import AuthTest

# Helps debugging
Config.log_enabled = True
# Config.dummy_run = True
# Config.client_execution_timeout = 300 * 1000
# Config.request_timeout = 300 * 1000
# Config.socket_timeout = 300 * 1000

policy_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy.txt')
policy = "file://" + os.path.abspath(policy_relative)

policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)

policy_condition_StringEquals_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_StringEquals_success.json')
policy_condition_StringEquals_success = "file://" + os.path.abspath(policy_condition_StringEquals_success_relative)

policy_condition_ArnLike_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_ArnLike_success.json')
policy_condition_ArnLike_success = "file://" + os.path.abspath(policy_condition_ArnLike_success_relative)

policy_condition_StringLike_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_StringLike_success.json')
policy_condition_StringLike_success = "file://" + os.path.abspath(policy_condition_StringLike_success_relative)

policy_condition_StringEqualsIfExists_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_StringEqualsIfExists_success.json')
policy_condition_StringEqualsIfExists_success = "file://" + os.path.abspath(policy_condition_StringEqualsIfExists_success_relative)

policy_condition_Bool_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_Bool_success.json')
policy_condition_Bool_success = "file://" + os.path.abspath(policy_condition_Bool_success_relative)

policy_condition_Bool_RandomKeyValue_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_Bool_RandomKeyValue_success.json')
policy_condition_Bool_RandomKeyValue_success = "file://" + os.path.abspath(policy_condition_Bool_RandomKeyValue_success_relative)

policy_condition_Bool_invalidKey_fail_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_Bool_invalidKey_fail.json')
policy_condition_Bool_invalidKey_fail = "file://" + os.path.abspath(policy_condition_Bool_invalidKey_fail_relative)

policy_condition_StringEquals_invalidKey_fail_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_StringEquals_invalidKey_fail.json')
policy_condition_StringEquals_invalidKey_fail = "file://" + os.path.abspath(policy_condition_StringEquals_invalidKey_fail_relative)

policy_condition_NumericLessThanEquals_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_NumericLessThanEquals_success.json')
policy_condition_NumericLessThanEquals_success = "file://" + os.path.abspath(policy_condition_NumericLessThanEquals_success_relative)

policy_condition_DateLessThan_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_DateLessThan_success.json')
policy_condition_DateLessThan_success = "file://" + os.path.abspath(policy_condition_DateLessThan_success_relative)

policy_condition_BinaryEquals_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_BinaryEquals_success.json')
policy_condition_BinaryEquals_success = "file://" + os.path.abspath(policy_condition_BinaryEquals_success_relative)

policy_condition_BinaryEquals_invalidValue_fail_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_BinaryEquals_invalidValue_fail.json')
policy_condition_BinaryEquals_invalidValue_fail = "file://" + os.path.abspath(policy_condition_BinaryEquals_invalidValue_fail_relative)

policy_condition_StringLike_invalidKey_fail_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_StringLike_invalidKey_fail.json')
policy_condition_StringLike_invalidKey_fail = "file://" + os.path.abspath(policy_condition_StringLike_invalidKey_fail_relative)

policy_condition_StringLikeIfExists_success_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_condition_StringLikeIfExists_success.json')
policy_condition_StringLikeIfExists_success = "file://" + os.path.abspath(policy_condition_StringLikeIfExists_success_relative)

AwsTest('Aws can create bucket').create_bucket("seagate").execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test(negative_case=True).command_should_fail().command_error_should_have("NoSuchBucketPolicy")

AwsTest("Aws can delete policy on bucket").delete_bucket_policy("seagate").execute_test().command_is_successful()

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("Resource")

AwsTest("Aws can delete policy on bucket").delete_bucket_policy("seagate").execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test(negative_case=True).command_should_fail().command_error_should_have("NoSuchBucketPolicy")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_put_bucket).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("Resource")

AwsTest("Aws can delete policy on bucket").delete_bucket_policy("seagate").execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test(negative_case=True).command_should_fail().command_error_should_have("NoSuchBucketPolicy")

#put-bucket-policy - Effect field absent
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_effect_missing.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with Effect field missing").put_bucket_policy("seagate", policy_put_bucket).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")


#put-bucket-policy - Resource-Action field unrelated
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_resource_action_unrelated.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with unrelated Resource and Action").put_bucket_policy("seagate", policy_put_bucket).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")


#put-bucket-policy - Action field accepts wild-card characters
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_action_with_wildcards.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with WildCard chars in Action").put_bucket_policy("seagate", policy_put_bucket).execute_test().command_is_successful()


#put-bucket-policy - Invalid field in policy
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_invalid_field_present.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with invalid field in policy json").put_bucket_policy("seagate", policy_put_bucket).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")


#put-bucket-policy - Fields not in order
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_improper_field_order.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with improper order of fields in policy json").put_bucket_policy("seagate", policy_put_bucket).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")


#put-bucket-policy - Multiple resources
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_with_multiple_resources.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with multiple resources in policy json").put_bucket_policy("seagate", policy_put_bucket).execute_test().command_is_successful()

#put-bucket-policy - Invalid Action
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_with_invalid_action.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with invalid Action in policy json").put_bucket_policy("seagate", policy_put_bucket).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")

#put-bucket-policy - Invalid Principal
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_invalid_principal.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with invalid Principal ID in policy json").put_bucket_policy("seagate", policy_put_bucket).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")


#put-bucket-policy - Valid principal
policy_put_bucket_relative = os.path.join(os.path.dirname(__file__), 'policy_files', 'policy_put_bucket_with_valid_principal.txt')
policy_put_bucket = "file://" + os.path.abspath(policy_put_bucket_relative)
AwsTest("Put Bucket Policy with valid Principal in policy json").put_bucket_policy("seagate", policy_put_bucket).execute_test().command_is_successful()

# Validate Conditions in Bucket Policy
AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_StringEquals_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("s3:x-amz-acl")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_ArnLike_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("aws:SourceArn")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_StringLike_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("s3:x-amz-acl")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_StringEqualsIfExists_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("s3:x-amz-acl")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_Bool_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("aws:SecureTransport")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_Bool_RandomKeyValue_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("aws:xyz")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_Bool_invalidKey_fail).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_StringEquals_invalidKey_fail).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_NumericLessThanEquals_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("s3:max-keys")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_DateLessThan_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("aws:CurrentTime")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_BinaryEquals_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("aws:key")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_BinaryEquals_invalidValue_fail).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_StringLike_invalidKey_fail).execute_test(negative_case=True).command_should_fail().command_error_should_have("MalformedPolicy")

AwsTest("Aws can put policy on bucket").put_bucket_policy("seagate", policy_condition_StringLikeIfExists_success).execute_test().command_is_successful()

AwsTest("Aws can get policy on bucket").get_bucket_policy("seagate").execute_test().command_is_successful().command_response_should_have("s3:x-amz-acl")

AwsTest('Aws can delete bucket seagate').delete_bucket("seagate").execute_test().command_is_successful()