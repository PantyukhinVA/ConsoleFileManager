import os
import messages
import functions
import victory


def test_create_new_dir_and_delete():
    path = functions.correct_name('test')
    if os.path.exists(path):
        functions.del_file_or_dir('test')

    assert (functions.create_new_dir('test') == messages.dir_created('test'))
    assert (functions.create_new_dir('test') == messages.dir_exists)
    assert (functions.del_file_or_dir('test') == messages.dir_correct_deleted('test'))
    assert (functions.del_file_or_dir('test') == messages.file_or_dir_not_exists)


def test_correct_list_stars():
    assert (len(victory.get_game_stars()) == 5)
