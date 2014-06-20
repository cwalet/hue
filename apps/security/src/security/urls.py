#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('security.views',
  url(r'^$', 'hive', name='index'),
  url(r'^hive$', 'hive', name='hive'),
  url(r'^hdfs$', 'hdfs', name='hdfs'),
)


urlpatterns += patterns('security.api',
  url(r'^api/get_acls$', 'get_acls', name='get_acls'),
)