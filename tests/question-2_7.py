test = {
  'name': 'question 2.7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(distances_list)==list
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'distances_list=distance(0.1, 0.6, 6)',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(distance(0.1, 0.6, 6), [[0.5019, 0.8076, 0.9171, 0.8304, 0.5475, 0.0684]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(distance(1, 6, 5, 3), [-6.81, -42.913125, -109.6725, -207.088125, -335.16])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
