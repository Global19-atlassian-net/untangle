#!/usr/bin/env python

import untangle


def access():
    o = untangle.parse('<node id="5">This is cdata<subnode value="abc"/></node>')
    return ("Node id = %s, subnode value = %s" %
            (o.node['id'], o.node.subnode['value']))


def siblings_list():
    o = untangle.parse('''
        <root>
            <child name="child1"/>
            <child name="child2"/>
            <child name="child3"/>
        </root>
        ''')
    return ','.join([child['name'] for child in o.root.child])

def access_cdata():
    o = untangle.parse('<node id="5">This is cdata<subnode value="abc"/></node>')
    return ("CDATA = %s" % (o.node.cdata))

examples = [
    ('Access children with parent.children and'
     ' attributes with element["attribute"]', access),
    ('Access siblings as list', siblings_list),
    ('Access cdata text or other data', access_cdata),
]

if __name__ == '__main__':
    for description, func in examples:
        print '=' * 70
        print description
        print '=' * 70
        print
        print func()
        print

# vim: set expandtab ts=4 sw=4:
