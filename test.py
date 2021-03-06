import os
import json

import tensorflow as tf

tf.app.flags.DEFINE_string('export_path', './data', 'path to data')

config_file = open(os.path.join('data', "config"), 'r')
config = json.loads(config_file.read())
config_file.close()

tf.app.flags.DEFINE_integer('max_length', config['fixlen'], 'maximum of number of words in one sentence')
tf.app.flags.DEFINE_integer('pos_num', config['maxlen'] * 2 + 1, 'number of position embedding vectors')
tf.app.flags.DEFINE_integer('num_classes', len(config['relation2id']), 'maximum of relations')

tf.app.flags.DEFINE_integer('hidden_size', 230, 'hidden feature size')
tf.app.flags.DEFINE_integer('pos_size', 5, 'position embedding size')
tf.app.flags.DEFINE_integer('word_size', 50, 'word embedding size')

tf.app.flags.DEFINE_integer('batch_size', 160, 'entity numbers used each training time')

tf.app.flags.DEFINE_string('checkpoint_dir', './checkpoint/', 'path to store checkpoint')
tf.app.flags.DEFINE_string('test_result_dir', './test_result', 'path to store the test results')

tf.app.flags.DEFINE_string('model_name', 'pcnn_att', 'model\'s name')
tf.app.flags.DEFINE_string('epoch_range', '(5, 60)', 'checkpoint epoch range')

tf.app.flags.DEFINE_float('drop_prob', 0.5, 'dropout rate')

FLAGS = tf.app.flags.FLAGS


def main(_):
    if not FLAGS.model_name in locals():
        exit()
    model = locals()[FLAGS.model_name]
    model(is_training=False)


if __name__ == "__main__":
    tf.app.run()
