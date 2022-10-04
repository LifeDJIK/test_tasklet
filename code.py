#!/usr/bin/python
# coding=utf-8
""" Task """

from pylon.core.tools import log  # pylint: disable=E0401


def execute(context, cleanup_directories):  # pylint: disable=R0914,R0912,R0915
    """ Task entry point """
    _ = context, cleanup_directories
    #
    log.info("Tasklet code started")
    log.info("Args: %s", context.args)
    #
    raise ValueError("My fault")
    #
    return 42
