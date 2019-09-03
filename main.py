import iterm2
from kubernetes import config

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Kubernetes Configuration",
        detailed_description="This tells you what your current kubernetes context and namespace are",
        exemplar="⎈ context:staging namespace:my-cluster",
        update_cadence=5,
        identifier="com.iterm2.jebentier.iterm2-kubernetes-context",
        knobs=[])

    @iterm2.StatusBarRPC
    async def coro(knobs):
        current_config = config.list_kube_config_contexts()[1]
        return "⎈ context:{} namespace:{}".format(current_config['name'], current_config['context']['namespace'])

    await component.async_register(connection, coro)

iterm2.run_forever(main)
