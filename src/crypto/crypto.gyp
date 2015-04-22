{
  'includes': [
    '../common.gypi',
  ],
  'variables': {
    'crypto_sources': [
      'hash.cc',
      'hash.h',
    ],
  },
  'targets': [
    {
      # The crypto library.
      'target_name': 'crypto',
      'type': '<(library)',
      'sources': [
        '<@(crypto_sources)',
      ],
      'target_defaults': {
        'cflags_cc+': [
        ],
        'xcode_settings': {
        },
      },
      'direct_dependent_settings': {
        'include_dirs': [
          '..',
        ],
      },
    },
    {
      # Unit tests for the monitor.
      'target_name': 'crypto_tests',
      'type': 'executable',
      'sources': [
        '<@(crypto_sources)',
        'hash_test.cc',
      ],
      'dependencies': [
        '../bare/bare.gyp:bare_testing',
        '../deps/gtest.gyp:gtest',
        '../deps/libcxx.gyp:libc++',
      ],
    },
  ],
}

