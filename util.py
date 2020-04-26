import numpy as np


def onehot_by_group(labels, groups, group_names=None):
    """
    One hot but assign binary value by group membership.
    For example: if (A, B) is considered one group, then a row having label A is assigned value 1
    :param labels: a list of labels
    :param groups: a list of groups
    :return:
    """

    if group_names is None:
        group_names = ['Group {}'.format(i) for i in range(1, len(groups)+1)]

    unique_labels = np.unique(labels)
    all_group_members = []
    for x in groups:
        all_group_members.extend(x)

    assert len(unique_labels) == len(all_group_members), 'unique labels = {}, but all_group_members = {}'.format(unique_labels, all_group_members)
    assert set(unique_labels) == set(all_group_members)
    assert len(group_names) == len(groups)

    map_onehot = {group_name: [] for group_name in group_names}

    for label in labels:
        for group, group_name in zip(groups, group_names):
            map_onehot[group_name].append(1 if label in group else 0)

    return map_onehot


def test_onehot_by_group():
    labels = ['A', 'B', 'C', 'A', 'C', 'B', 'B']
    groups = (('A', 'B'), ('C'))
    group_names = ('AB', 'C')
    expected = {'AB': [1, 1, 0, 1, 0, 1, 1], 'C': [0, 0, 1, 0, 1, 0, 0]}

    result = onehot_by_group(labels, groups, group_names)

    print(result)
    print(expected)

if __name__ == '__main__':
    test_onehot_by_group()