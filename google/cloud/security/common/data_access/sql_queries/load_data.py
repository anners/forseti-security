# Copyright 2017 The Forseti Security Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""SQL queries to load data into snapshot tables."""

LOAD_DATA = """
    LOAD DATA LOCAL INFILE '{0}'
    INTO TABLE {1} FIELDS TERMINATED BY ','
    ({2});
"""

INSERT_VIOLATION = """
    INSERT INTO {0}
    (violation_hash, resource_type, resource_id, rule_name, rule_index,
     violation_type, violation_data, created_at_datetime)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
