#!/usr/bin/python
# encoding: utf-8
#
# Copyright (C) 2015 Ian McLeod <imcleod@redhat.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation;
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# This dumps the header and dynamic header of a presumed VHD file

import struct
import sys

# Header/Footer - From MS doco
# 512 bytes - early versions had a 511 byte footer for no obvious reason

#Cookie 8
#Features 4
#File Format Version 4
#Data Offset 8
#Time Stamp 4
#Creator Application 4
#Creator Version 4
#Creator Host OS 4
#Original Size 8
#Current Size 8
#Disk Geometry 4
# Disk Cylinders 2
# Disk Heads 1
# Disk Sectors 1
#Disk Type 4
#Checksum 4
#Unique Id 16
#Saved State 1
#Reserved 427

HEADER_FMT = ">8sIIQI4sIIQQHBBII16sB427s"

# Dynamic header
# 1024 bytes

#Cookie 8
#Data Offset 8
#Table Offset 8
#Header Version 4
#Max Table Entries 4
#Block Size 4
#Checksum 4
#Parent Unique ID 16
#Parent Time Stamp 4
#Reserved 4
#Parent Unicode Name 512
#Parent Locator Entry 1 24
#Parent Locator Entry 2 24
#Parent Locator Entry 3 24
#Parent Locator Entry 4 24
#Parent Locator Entry 5 24
#Parent Locator Entry 6 24
#Parent Locator Entry 7 24
#Parent Locator Entry 8 24
#Reserved 256

DYNAMIC_FMT = ">8sQQIIII16sII512s192s256s"

f = open(sys.argv[1])

hdr = f.read(512)
dhdr = f.read(1024)

[ cookie, features, fmt_version, data_offset, timestamp,
    creator_app, creator_ver, creator_os, orig_size, curr_size, disk_c, disk_h,
    disk_s, disk_type, checksum, my_uuid, saved_state, reserved ] = struct.unpack(HEADER_FMT, hdr)

#header = struct.unpack(HEADER_FMT, hdr)
#print header

print "**** Header ****"
print "cookie: %s" % (cookie)
print "features: %d" % (features)
print "fmt_version: %d" % (fmt_version)
print "data_offset: %d" % (data_offset)
print "timestamp: %d" % (timestamp)
print "creator_app: %s" % (creator_app)
print "creator_ver: %d" % (creator_ver)
print "creator_os: %d" % (creator_os)
print "orig_size: %d" % (orig_size)
print "curr_size: %d" % (curr_size)
print "disk_c: %d" % (disk_c)
print "disk_h: %d" % (disk_h)
print "disk_s: %d" % (disk_s)
print "disk_type: %d" % (disk_type)
print "checksum: %d" % (checksum)
print "my_uuid: %s" % (my_uuid)
print "saved_state: %s" % (saved_state)


[ cookie2, data_offset2, table_offset, header_version,
    max_table_entries, block_size, checksum2, parent_uuid, parent_timestamp,
    reserved2, parent_name, parent_locents, reserved3 ] = struct.unpack(DYNAMIC_FMT, dhdr)

#dynheader = struct.unpack(DYNAMIC_FMT, dhdr)
#print dynheader

print
print "**** Dynamic Header ****"
print "cookie: %s" % (cookie2)
print "data_offset: %d" % (data_offset2)
print "table_offset: %d" % (table_offset)
print "header_version: %d" % (header_version)
print "max_table_entries: %d" % (max_table_entries)
print "block_size: %d" % (block_size)
print "checksum: %d" % (checksum2)
print "parent_uuid: %s" % (parent_uuid)
print "parent_timestamp: %d" % (parent_timestamp)
